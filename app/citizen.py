import httpx
from fastapi import HTTPException


async def fetch_citizen_details(cid: str):
    # Replace the URL below with the actual API endpoint
    api_url = f"https://api.example.com/citizens/{cid}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            citizen_data = response.json()
            return citizen_data
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code,
                            detail="Failed to fetch citizen details")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
