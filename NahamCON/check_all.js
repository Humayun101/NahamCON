const WebSocket = require('ws');

const TOTAL_BOXES = 2_000_000;
const BATCH_SIZE = 500;
const DELAY_MS = 50;  // delay between batch sends

let ws;
let currentIndex = 0;

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function sendBatches() {
  while (currentIndex < TOTAL_BOXES) {
    const start = currentIndex;
    const end = Math.min(start + BATCH_SIZE, TOTAL_BOXES);

    const numbers = [];
    for (let i = start; i < end; i++) {
      numbers.push(i);
    }

    ws.send(JSON.stringify({
      action: 'check',
      numbers: numbers,
    }));

    console.log(`Sent batch: ${start} to ${end - 1}`);

    currentIndex = end;
    await delay(DELAY_MS);  // wait before sending next batch
  }
  console.log('All batches sent!');
}

function connect() {
  ws = new WebSocket('ws://challenge.nahamcon.com:30948/ws');

  ws.on('open', () => {
    console.log('Connected to server. Starting to check boxes...');
    sendBatches();
  });

  ws.on('message', (data) => {
    // You can log server messages if you want
    // console.log('Server:', data.toString());
  });

  ws.on('close', () => {
    console.log('Connection closed.');
  });

  ws.on('error', (err) => {
    console.error('WebSocket error:', err);
  });
}

connect();
