from mcp.server.fastmcp import Fastmcp
from app import get_realtime_info, generate_video_script

mcp = Fastmcp("Video Script Generator")

@mcp.tool()
async def get_latest_info_mcp(query):
    return get_realtime_info(query)

@mcp.tool()
async def generate_video_script(real_info):
    real_info =  get_realtime_info(real_info)
    return generate_video_script(real_info)

if __name__ == "__main__":
    mcp.run(transport='stdio')