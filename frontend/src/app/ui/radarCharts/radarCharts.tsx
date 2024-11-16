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

// Регистрация компонентов
ChartJS.register(RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend);

const RadarCharts = ({ points }: { points: number[] }) => {
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
      'Организаторские способности',
      'Результативность труда',
      'Работа в команде',
    ],
    datasets: [
      {
        data: [3, 1, 2, 6, 9, 3.4, 9, 5.4, 7, 8, 5.3, 1.1], // Значения по каждой характеристике
        backgroundColor: 'rgba(242, 84, 48, 0.2)', // Заливка
        borderColor: 'rgba(242, 84, 48, 1)', // Цвет границы
        borderWidth: 1, // Толщина границы
      },
    ],
  };

  // Опции диаграммы
  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        enabled: true, // Всплывающие подсказки
      },
    },
    scales: {
      r: {
        beginAtZero: true, // Начало шкалы с нуля
        suggestedMax: 10, // Максимальное значение шкалы
        ticks: {
          stepSize: 1, // Шаг между значениями
        },
      },
    },
  };

  return (
    <div style={{ width: '500px', height: '500px', margin: '0 auto' }}>
      <Radar data={data} options={options} />
    </div>
  );
};

export default RadarCharts;
