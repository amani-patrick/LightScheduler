const socket = new WebSocket('ws://localhost:8765');
const statusDisplay = document.getElementById('status');

socket.addEventListener('open', () => {
  statusDisplay.textContent = 'Status: Connected to server';
  statusDisplay.title = 'Connected to server. You can proceed with scheduling.';
});

socket.addEventListener('message', (event) => {
  statusDisplay.textContent = `Status: ${event.data}`;
  statusDisplay.title = 'Connected to server. You can proceed with scheduling.';
});

socket.addEventListener('close', () => {
  statusDisplay.textContent = 'Status: Disconnected from server';
  statusDisplay.title = 'Disconnected from server. Please run subscriber.py to reconnect.';
});

function submitSchedule() {
  const onTimeInput = document.getElementById('on-time').value;
  const offTimeInput = document.getElementById('off-time').value;

  if (!onTimeInput || !offTimeInput) {
    statusDisplay.textContent = 'Status: Please select both ON and OFF times';
    return;
  }

  const schedulePayload = {
    onTime: onTimeInput,
    offTime: offTimeInput,
  };

  socket.send(JSON.stringify(schedulePayload));
  statusDisplay.textContent = 'Status: Schedule sent';
}