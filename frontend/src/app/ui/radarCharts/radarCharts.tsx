import React from 'react';
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
} from 'chart.js';
import { Radar } from 'react-chartjs-2';

ChartJS.register(RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend);

const RadarCharts = ({ points }: { points: number[] }) => {
  console.log(points);

  const data = {
    labels: [
      'Стрессоустойчивость',
      'Гибкость',
      'Коммуникабельность',
      'Креативность',
      'Инициативность',
      'Лидерские качества',
      'Профессиональная компетентность',
      'Умение принимать решения',
      'Трудолюбивость',
      'Координирование',
      'Результативность труда',
      'Работа в команде',
    ],
    datasets: [
      {
        data: points,
        backgroundColor: 'rgba(242, 84, 48, 0.2)',
        borderColor: 'rgba(242, 84, 48, 1)',
        borderWidth: 1,
      },
    ],
  };
  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        enabled: true,
      },
    },
    scales: {
      r: {
        beginAtZero: true,
        suggestedMax: 10,
        ticks: {
          stepSize: 1,
        },
      },
    },
  };
  return (
    <div style={{ width: '550px', height: '550px', margin: '0 auto' }}>
      <Radar data={data} options={options} />
    </div>
  );
};

export default RadarCharts;
