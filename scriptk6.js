import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    scenarios: {
        authorization: {
            executor: 'ramping-vus',
            exec: 'Authorization',
            startVUS: 0,
            stage: [
                {duration: '20s', target: 25},
                {duration: '2s', target: 5}
            ]
        },

        users: {
            executor: 'per-vu-iterations',
            exec: 'Users',
            vus: 1,
            iterations: 1,
            startTime: '1s'
        }
    },

    thresholds: {
        http_req_duration: ['p(95) < 250'],
        http_req_failed: ['rate<=0.05']
    }
}

export function Authorization() {
    let url = "https://httbin.org/post"
    let payload = JSON.stringify({
        login: "test",
        password: "password"
    })

    const request = http.post(url, payload);

    check(res, {
        'status code = 200' : (r) => r.status == 200,
        'body includes password' : (r) => r.body.includes("password"),
    })
}