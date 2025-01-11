
from config.config import Config
from model.graph_entity.node_io_processor_thread import NodeIOProcessor as ThreadNodeIOProcessor
from model.graph_entity.node_io_processor_coroutine import NodeIOProcessor as CoroutineNodeIOProcessor

__async_mode = Config.get_instance().get_with_nested_params("cache", "async")
if __async_mode == "thread":
    NODE_ASYNC_IO = ThreadNodeIOProcessor()
else:
    NODE_ASYNC_IO = CoroutineNodeIOProcessor()
