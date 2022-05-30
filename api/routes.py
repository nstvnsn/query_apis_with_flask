from flask import request

from api.utils.routes import query_api_endpoint
from api.wsgi import app


@app.route("/api/ping", methods=["GET"])
def ping():
    return {"success": True}, 200


@app.route("/api/posts", methods=["GET"])
async def posts():
    tags = request.args.get("tags")
    sort_by = request.args.get("sortBy") or "id"
    direction = request.args.get("direction") or "asc"

    if not request.args.get("tags"):
        return {"error": "Tags parameter is required"}, 400
    else:
        tags = request.args.get("tags").split(",")

    if sort_by not in ["id", "reads", "likes", "popularity"]:
        return {"error": "sortBy parameter is invalid"}, 400

    sorted_posts_list = await query_api_endpoint(tags=tags, sort_by=sort_by, direction=direction)

    return {"posts": sorted_posts_list}
