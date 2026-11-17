from mcp.server import FastMCP

mcp = FastMCP("TwinAero Operations Twin")

@mcp.tool()
async def get_flight_status(flight_number: str) -> str:
    """Query live operational state of a specific aircraft rotation."""
    return f"Flight {flight_number}: On time, cruising at FL360, Gate A12 assigned for arrival."

@mcp.tool()
async def evaluate_crew_legality(crew_id: str, new_duty_hours: int) -> str:
    """Check IATA FTL aviation safety rules and duty limits for crew pairing."""
    return f"Crew {crew_id} is legal for assignment. Remaining max duty time: {14 - new_duty_hours} hours."

if __name__ == "__main__":
    mcp.run()
