
from mcp.server.fastmcp import FastMCP


server = FastMCP('weather_server')



@server.tool()
async def get_alerts(city: str) -> str:
    """Get alerts for a city
    
    Args:
        city: The city to get alerts for
    Returns:
        A string indicating that the alerts have been retrieved successfully
    """
    res = f"Getting alerts for {city}: Success!"
    return res


@server.tool()
async def get_forecast(city: str) -> str:
    """Get forecast for a city
    
    Args:
        city: The city to get forecast for
    Returns:
        A string indicating that the forecast has been retrieved successfully
    """
    res = f"Getting forecast for {city}: Success!"
    return res


if __name__ == "__main__":
    server.run(transport='stdio')
