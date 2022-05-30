import aiohttp, asyncio

API = "INSERT API HERE"

recent_pulls = []


async def query_api_aiohttp_request(url: str, session: aiohttp.ClientSession) -> dict:
    async with session.get(url) as resp:
        return await resp.json()


def remove_duplicates_by_key(dict_list: list[dict], key: str = "id") -> list:
    cleaned_list = []
    unique_keys = set()

    for dictObj in dict_list:
        if dictObj[key] in unique_keys:
            continue
        unique_keys.add(dictObj[key])
        cleaned_list.append(dictObj)
    return cleaned_list


async def multi_query_given_tags(session: aiohttp.ClientSession, api_url: str, tags: list[str], **kwargs) -> list:
    tasks = []

    for tag in tags:
        request_url = f"""{api_url}?tag={tag}&sortBy={kwargs["sort_by"]}&direction={kwargs["direction"]}"""
        tasks.append(query_api_aiohttp_request(request_url, session))

    gathered_results_list = await asyncio.gather(*tasks)

    return gathered_results_list


async def query_api_endpoint(tags: list[str], sort_by: str, direction: str) -> list:
    async with aiohttp.ClientSession() as session:
        posts_list = []

        gathered_results = await multi_query_given_tags(session, API, tags, sort_by=sort_by, direction=direction)

        for result in gathered_results:
            posts_list.extend(result["posts"])

        cleaned_list = remove_duplicates_by_key(posts_list, sort_by)

        return sorted(cleaned_list, key=lambda item: item[sort_by], reverse=(direction == "desc"))
