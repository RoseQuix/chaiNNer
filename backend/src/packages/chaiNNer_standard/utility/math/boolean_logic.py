from __future__ import annotations

from enum import Enum
from typing import Dict, Union

from nodes.groups import if_enum_group
from nodes.properties.inputs import EnumInput, NumberInput, BoolInput
from nodes.properties.outputs import BoolOutput
from .. import math_group


class BoolOperation(Enum):
    And = "and"
    Or = "or"
    Xor = "xor"
    Not = "not"


OP_LABEL: Dict[BoolOperation, str] = {
    BoolOperation.And: "And: a ∧ b",
    BoolOperation.Or: "Logical Or: a ∨ b",
    BoolOperation.Xor: "Exclusive Or: a ⊕ b",
    BoolOperation.Not: "Not: ¬a",
}


@math_group.register(
    schema_id="chainner:utility:boollogic",
    name="Logic",
    description="Logical operators",
    icon="MdJoinRight",
    inputs=[
        BoolInput(
            "Operand a",
            has_handle=True,
        ),
        EnumInput(BoolOperation, "Boolean Operation", option_labels=OP_LABEL).with_id(1),
        if_enum_group(1, [BoolOperation.And, BoolOperation.Or, BoolOperation.Xor])(
            BoolInput(
                "Operand b",
                has_handle=True,
            ),
        )
    ],
    outputs=[
        BoolOutput(
            label="Result",
            output_type="""
                let a = Input0;
                let b = Input2;

                match Input1 {
                    BoolOperation::And => a & b,
                    BoolOperation::Or  => a | b,
                    BoolOperation::Xor => a != b,
                    BoolOperation::Not => a != true,
                }
                """,
        ),
    ],
)
def comparison_node(a: bool, op: BoolOperation, b: bool) -> bool:
    if op == BoolOperation.And:
        return a and b
    elif op == BoolOperation.Or:
        return a or b
    elif op == BoolOperation.Xor:
        return a != b
    elif op == BoolOperation.Not:
        return not a
    else:
        raise RuntimeError(f"Unknown operator {op}")
