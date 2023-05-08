from __future__ import annotations

from enum import Enum
from typing import Dict, Union

from nodes.properties.inputs import EnumInput, NumberInput
from nodes.properties.outputs import BoolOutput
from .. import math_group


class TestOperation(Enum):
    Lte = "lte"
    Lt = "lt"
    Gte = "gte"
    Gt = "gt"
    Eq = "eq"
    Neq = "neq"


OP_LABEL: Dict[TestOperation, str] = {
    TestOperation.Lte: "Test: a ≤ b",
    TestOperation.Lt: "Test: a < b",
    TestOperation.Gte: "Test: a ≥ b",
    TestOperation.Gt: "Test: a > b",
    TestOperation.Eq: "Test: a = b",
    TestOperation.Neq: "Test: a ≠ b",
}


@math_group.register(
    schema_id="chainner:utility:compare",
    name="Compare",
    description="Compare two numbers",
    icon="MdCompareArrows",
    inputs=[
        NumberInput(
            "Operand a",
            minimum=None,
            maximum=None,
            precision=100,
            controls_step=1,
        ),
        EnumInput(TestOperation, "Test Operation", option_labels=OP_LABEL),
        NumberInput(
            "Operand b",
            minimum=None,
            maximum=None,
            precision=100,
            controls_step=1,
        ),
    ],
    outputs=[
        BoolOutput(
            label="Result",
            output_type="""
                let a = Input0;
                let b = Input2;

                match Input1 {
                    TestOperation::Lte => a <= b,
                    TestOperation::Lt  => a < b,
                    TestOperation::Gte => a >= b,
                    TestOperation::Gt  => a > b,
                    TestOperation::Eq  => a == b,
                    TestOperation::Neq => a != b,
                }
                """,
        ),
    ],
)
def comparison_node(a: float, op: TestOperation, b: float) -> Union[int, float]:
    if op == TestOperation.Lte:
        return a <= b
    elif op == TestOperation.Lt:
        return a < b
    elif op == TestOperation.Gte:
        return a >= b
    elif op == TestOperation.Gt:
        return a > b
    elif op == TestOperation.Eq:
        return a == b
    elif op == TestOperation.Neq:
        return a != b
    else:
        raise RuntimeError(f"Unknown operator {op}")
