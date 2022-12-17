import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    {duration: '30s', target: 20},
    {duration: '5s', target: 10},
    {duration: '10s', target: 50}
  ],
}

export default function () {
  const request = http.get('https://test.k6.io');
  check(request, {'status = 200': (r) => r.status == 200 });
  sleep(1);
}
