import logging
import apie
import eons

class operation_implementation(apie.Endpoint):
    def __init__(this, name="Implementation for Operation Endpoints", implements=eons.INVALID_NAME()):
        super().__init__(name)

        this.implements = implements
        this.implemented = None

        # Everything that can change an operation's implementation should be specified somewhere in apie, not in the request.
        # By prepending this.implements, we can have multiple implementations which use very similar args (e.g. external url).
        this.fetchFrom = [
            'this',
            'args',
            'precursor_implements_prepended',
            'executor_implements_prepended',
            'environment_implements_prepended',
            'precursor',
            'executor',
            'environment',
        ]

        this.allowedNext.append(this.implements)


    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return '''\
Provide an implementation for downstream resources.
Should not be called directly.
'''

    # Enable Fetching values prepended with what *this implements.
    # This makes it possible to specify "first_implements_arg" and "second_implements_arg" independently (as opposed to both being just "arg")
    def fetch_location_precursor_implements_prepended(this, varName, default, fetchFrom, attempted):
        
        return this.fetch_location_precursor(f"{this.implements}_{varName}", default, fetchFrom, attempted)

    # Enable Fetching values prepended with what *this implements.
    # This makes it possible to specify "first_implements_arg" and "second_implements_arg" independently (as opposed to both being just "arg")
    def fetch_location_executor_implements_prepended(this, varName, default, fetchFrom, attempted):
        
        return this.fetch_location_executor(f"{this.implements}_{varName}", default, fetchFrom, attempted)

    # Enable Fetching values prepended with what *this implements.
    # This makes it possible to specify "first_implements_arg" and "second_implements_arg" independently (as opposed to both being just "arg")
    def fetch_location_environment_implements_prepended(this, varName, default, fetchFrom, attempted):
        
        return this.fetch_location_environment(f"{this.implements}_{varName}", default, fetchFrom, attempted)
