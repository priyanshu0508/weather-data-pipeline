from datetime import datetime, timedelta
from db.factory import get_db_client

def pipeline_health_check():
    status = {
        "status": "UNKNOWN",
        "last_ingestion": None,
        "checked_at": datetime.utcnow().isoformat()
    }

    try:
        db = get_db_client()
        last = db.get_last_ingestion_time()

        if not last:
            status["status"] = "NO DATA"
            return status

        status["last_ingestion"] = last

        last_dt = datetime.fromisoformat(last)
        if datetime.utcnow() - last_dt > timedelta(hours=2):
            status["status"] = "STALE DATA"
        else:
            status["status"] = "HEALTHY"

    except Exception as e:
        status["status"] = "ERROR"
        status["error"] = str(e)

    return status
