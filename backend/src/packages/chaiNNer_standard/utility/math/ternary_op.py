from __future__ import annotations

from nodes.properties.inputs import BoolInput, AnyInput
from nodes.properties.outputs import BaseOutput
from .. import math_group


@math_group.register(
    schema_id="chainner:utility:ternary",
    name="Conditional",
    description="Select a value based on a boolean input",
    icon="MdQuiz",
    inputs=[
        BoolInput("Test", has_handle=True),
        AnyInput("When True"),
        AnyInput("When False"),
    ],
    outputs=[
        BaseOutput(
            label="Value",
            output_type="""
                match Input0 {
                    true  => Input1,
                    false => Input2,
                }
            """
        )
    ],
)
def conditional_node(test: bool, when_true: object, when_false: object) -> object:
    return when_true if test else when_false
