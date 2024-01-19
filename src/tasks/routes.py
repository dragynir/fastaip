from fastapi import APIRouter, Depends

from auth.base_config import current_user
from tasks.tasks import send_email_report_dashboard

tasks_router = APIRouter(prefix='/report')


@tasks_router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard(user.username)
    return {
        'status': 200,
        'data': 'Send email.',
        'details': None
    }
