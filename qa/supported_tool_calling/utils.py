
import dataclasses

from openai import Stream
from openai.types.chat import ChatCompletionChunk


@dataclasses.dataclass
class ChatResponse:
    chunks: Stream[ChatCompletionChunk] | str | None = None
    prefix: str = ""
    suffix: str = ""

    def __call__(self, *args, **kwargs):
        partial_message = ""
        if self.chunks:
            for chunk in self.chunks:
                partial_message = partial_message + (chunk.choices[0].delta.content or "")
                yield partial_message

        yield self.prefix + partial_message + self.suffix
