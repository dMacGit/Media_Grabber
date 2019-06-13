from core import start_app_Threads, initialize, shutdown

"""Need to call functions in this order:
- init_app_Threads()
- start_app_Threads() <- When starting server
- initialize() <- starts server logic

When shutting down:
- shutdown()
"""
start_app_Threads()
initialize()
# Wait for termination
