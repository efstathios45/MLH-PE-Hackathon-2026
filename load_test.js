import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  // Bronze Tier Objective: 50 concurrent users
  vus: 50, 
  duration: '30s',
};

export default function () {
  // This hits the endpoint you just verified in your browser
  const res = http.get('http://127.0.0.1:5000/api/urls/');

  // Optional: This checks if the server is returning 200 OK
  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  // Each virtual user waits 1 second between requests
  sleep(1);
}