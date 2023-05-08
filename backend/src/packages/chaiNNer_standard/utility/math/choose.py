from __future__ import annotations

from typing import Union

from nodes.group import group
from nodes.properties.inputs import BoolInput, AnyInput, NumberInput
from nodes.properties.outputs import BaseOutput
from .. import math_group


@math_group.register(
    schema_id="chainner:utility:choose",
    name="Choose (Index)",
    description="Select a value based on an integer input",
    icon="MdList",
    inputs=[
        NumberInput(
            "Index",
            default=1,
            precision=0,
            minimum=1,
            maximum=10,
            controls_step=1
        ),
        AnyInput("Option 1"),
        group("optional-list")(
            *[AnyInput(f"Option {idx}").make_optional() for idx in range(2, 11)],
        ),
    ],
    outputs=[
        BaseOutput(
            label="Value",
            output_type="""
                match Input0 {
                    1  => Input1,
                    2  => Input2,
                    3  => Input3,
                    4  => Input4,
                    5  => Input5,
                    6  => Input6,
                    7  => Input7,
                    8  => Input8,
                    9  => Input9,
                    10 => Input10,
                }
            """
        )
    ],
)
def choose_node(idx: bool, *args: Union[object, None]) -> object:
    return args[idx - 1]
