from fastapi import APIRouter, Depends, BackgroundTasks

from auth.base_config import current_user
from tasks.tasks import send_email_report_dashboard

tasks_router = APIRouter(prefix='/report')


@tasks_router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    return {
        'status': 200,
        'data': 'Send email.',
        'details': None
    }


@tasks_router.get("/dashboard_bg_task")
def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    background_tasks.add_task(send_email_report_dashboard, user.username)
    return {
        'status': 200,
        'data': 'Send email.',
        'details': None
    }
