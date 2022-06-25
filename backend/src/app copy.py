from fastapi import FastAPI
import uuid
from typing import List

import asyncio

context = {'jobs': {}}

app = FastAPI()


async def do_work(job_key, files=None):
    iter_over = files if files else range(100)
    for file, file_number in enumerate(iter_over):
        jobs = context['jobs']
        job_info = jobs[job_key]
        job_info['iteration'] = file_number
        job_info['status'] = 'inprogress'
        await asyncio.sleep(1)
    # pending_jobs[job_key]['status'] = 'done'


@app.get('/')
async def get_testing():
    identifier = str(uuid.uuid4())
    context['jobs'][identifier] = {}
    asyncio.run_coroutine_threadsafe(do_work(identifier),
                                     loop=asyncio.get_running_loop())

    return {"identifier": identifier}


@app.get('/status')
def status():
    return {
        'all': list(context['jobs'].values()),
    }


@app.get('/status/{identifier}')
async def status(identifier):
    return {
        "status":
        context['jobs'].get(identifier,
                            'job with that identifier is undefined'),
    }
