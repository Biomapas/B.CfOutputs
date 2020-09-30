from b_cf_outputs.cf_stacks import CfStacks
from b_cf_outputs_test.mocks.boto_session_mock import BotoSessionMock


def test_FUNC_get_stacks_WITH_existing_stacks_EXPECT_stacks_returned() -> None:
    """
    Check if the function can list stacks.

    :return: No return.
    """
    stacks = list(CfStacks(BotoSessionMock()).get_stacks())

    assert stacks[0] == 'TestStackName'
