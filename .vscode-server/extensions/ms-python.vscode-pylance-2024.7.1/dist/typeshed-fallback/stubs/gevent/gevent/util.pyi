from _typeshed import SupportsWrite
from collections.abc import Callable
from types import TracebackType
from typing import Any, Generic, TypeVar
from typing_extensions import ParamSpec, Self

from gevent.hub import Hub
from greenlet import greenlet as greenlet_t

_T = TypeVar("_T")
_P = ParamSpec("_P")

class wrap_errors(Generic[_P, _T]):
    def __init__(self, errors: tuple[type[BaseException], ...], func: Callable[_P, _T]) -> None: ...
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _T: ...
    def __getattr__(self, name: str) -> Any: ...

def print_run_info(
    thread_stacks: bool = True, greenlet_stacks: bool = True, limit: int | None = ..., file: SupportsWrite[str] | None = None
) -> None: ...
def format_run_info(
    thread_stacks: bool = True, greenlet_stacks: bool = True, limit: int | None = ..., current_thread_ident: int | None = None
) -> None: ...

class GreenletTree:
    greenlet: greenlet_t | None
    is_current_tree: bool
    child_trees: list[GreenletTree]
    DEFAULT_DETAILS: dict[str, Any]
    def __init__(self, greenlet: greenlet_t | None) -> None: ...
    def add_child(self, tree: GreenletTree) -> None: ...
    @property
    def root(self) -> bool: ...
    def __getattr__(self, name: str) -> Any: ...
    def format_lines(self, details: bool | dict[str, Any] = True) -> str: ...
    def format(self, details: bool | dict[str, Any] = True) -> str: ...
    @classmethod
    def forest(cls) -> list[GreenletTree]: ...
    @classmethod
    def current_tree(cls) -> GreenletTree: ...

class assert_switches:
    hub: Hub | None
    tracer: object | None
    max_blocking_time: float | None
    hub_only: bool
    def __init__(self, max_blocking_time: float | None = None, hub_only: bool = False) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...
