import ClassRoom from './0-classroom.js';

// Function to initialize an array of ClassRoom objects with predefined sizes
export default function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
}
