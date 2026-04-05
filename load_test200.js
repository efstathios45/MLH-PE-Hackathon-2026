import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  // Silver Tier Objective: 200 concurrent users
  vus: 200, 
  duration: '30s',
};

export default function () {
  // We hit port 80 (Nginx), which then distributes to our 3 web clones
  const res = http.get('http://localhost/api/urls/');

  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1);
}