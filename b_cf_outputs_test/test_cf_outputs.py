from b_cf_outputs.cf_outputs import CfOutputs
from b_cf_outputs_test.mocks.boto_session_mock import BotoSessionMock


def test_FUNC_get_outputs_WITH_existing_stacks_EXPECT_outputs_returned() -> None:
    """
    Check if the function can return stack outputs.

    :return: No return.
    """
    outputs = CfOutputs(BotoSessionMock()).get_outputs()

    assert outputs['TestStackName']['key'] == 'value'
