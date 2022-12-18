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

    check(request, {
        'status code = 200' : (r) => r.status == 200,
        'body includes password' : (r) => r.body.includes("password"),
    })

    sleep(2);
}

export function Users() {
    let request = http.get("http://jsonplaceholder.typicode.com/users")
    check(request, {
        'body is not empty' : (r) => r.body.length > 0
    })
}

