import css from './staffBlock.module.css';

export const StaffBlock = () => {
  return (
    <div className={css.main__container}>
      <b>Бубнов Виталий</b>
      <span>Продуктовый менеджер</span>
      <span>5 лет опыта</span>
      <span>Отдел IТ-продуктов</span>
      <button className={css.parcel__button}>Смотреть расклад</button>
    </div>
  );
};
