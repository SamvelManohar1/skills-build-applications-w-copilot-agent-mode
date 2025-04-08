import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('https://vigilant-space-waffle-wqw79g44jv42gjwq-8000.app.github.dev/api/workouts/')
      .then(response => response.json())
      .then(data => setWorkouts(data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div className="card">
      <div className="card-header">Workouts</div>
      <ul className="list-group list-group-flush">
        {workouts.map(workout => (
          <li key={workout._id} className="list-group-item">
            <strong>{workout.name}</strong>: {workout.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Workouts;
