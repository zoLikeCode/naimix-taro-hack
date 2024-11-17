'use client';

import {
  useChooseEmployment,
  useChooseExperience,
  useChooseSchedule,
  useChooseSort,
  useShowCount,
} from '@/app/store';
import css from './filters.module.css';
import { useState } from 'react';
import { PopupFilter } from '../popupFilter/popupFilter';

export const Filtres = () => {
  const { count, setCount } = useShowCount();
  const { experience, setExperience } = useChooseExperience();
  const { employment, setEmployment } = useChooseEmployment();
  const { schedule, setSchedule } = useChooseSchedule();
  const { sort, setSort } = useChooseSort();

  const [value, setValue] = useState<string>('');

  const exp: string[] = ['Опыт работы', 'Без опыта', '1-2 года', '3-5 лет', '6+ лет'];
  const emp: string[] = ['Занятость', 'Полная', 'Частичная', 'Проектная', 'Удаленно'];
  const sch: string[] = [
    'График',
    'Полный день',
    'Неполный день',
    'Гибкий график',
    'Сменный график',
    'Вахтовый метод',
  ];
  const cnt: number[] = [10, 15, 20];
  const srt: string[] = ['Сначала новые', 'Сначала старые'];

  const [activePopupCount, setActivePopupCount] = useState<boolean>(false);
  const [activePopupExperience, setActivePopupExperience] = useState<boolean>(false);
  const [activePopupEmployment, setActivePopupEmployment] = useState<boolean>(false);
  const [activePopupSchedule, setActivePopupSchedule] = useState<boolean>(false);
  const [activePopupSort, setActivePopupSort] = useState<boolean>(false);

  return (
    <div className={css.main__container}>
      <form className={css.form__content}>
        <input
          className={css.input__content}
          placeholder="Профессия, город..."
          onChange={(e) => {
            setValue(e.target.value);
          }}
        />
      </form>
      <button
        type="button"
        className={css.button__popup}
        onClick={() => {
          setActivePopupExperience(!activePopupExperience);
        }}
      >
        {experience}
      </button>
      <button
        type="button"
        className={css.button__popup}
        onClick={() => {
          setActivePopupEmployment(!activePopupEmployment);
        }}
      >
        {employment}
      </button>
      <button
        type="button"
        className={css.button__popup}
        onClick={() => {
          setActivePopupSchedule(!activePopupSchedule);
        }}
      >
        {schedule}
      </button>
      <button
        type="button"
        className={css.button__popup__count}
        onClick={() => {
          setActivePopupCount(!activePopupCount);
        }}
      >
        {count}
      </button>
      <button
        type="button"
        className={css.button__popup}
        onClick={() => {
          setActivePopupSort(!activePopupSort);
        }}
      >
        {sort}
      </button>
      <span className={css.popupfilter__experience}>
        <PopupFilter
          type="str"
          active={activePopupExperience}
          setActive={setActivePopupExperience}
          data={exp}
          store={experience}
          setStore={setExperience}
        />
      </span>
      <span className={css.popupfilter__employment}>
        <PopupFilter
          type="str"
          active={activePopupEmployment}
          setActive={setActivePopupEmployment}
          data={emp}
          store={employment}
          setStore={setEmployment}
        />
      </span>
      <span className={css.popupFilter__schedule}>
        <PopupFilter
          type="str"
          active={activePopupSchedule}
          setActive={setActivePopupSchedule}
          data={sch}
          store={schedule}
          setStore={setSchedule}
        />
      </span>
      <span className={css.popupFilter__count}>
        <PopupFilter
          type="num"
          active={activePopupCount}
          setActive={setActivePopupCount}
          data={cnt}
          store={count}
          setStore={setCount}
        />
      </span>
      <span className={css.popupFilter__sort}>
        <PopupFilter
          type="str"
          active={activePopupSort}
          setActive={setActivePopupSort}
          data={srt}
          store={sort}
          setStore={setSort}
        />
      </span>
    </div>
  );
};
