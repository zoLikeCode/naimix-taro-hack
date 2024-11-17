import { SortArrow } from '../../../../public/SortArrow';
import css from './attrbText.module.css';

export const AttrbText = () => {
  return (
    <ul className={css.main__container}>
      <li className={css.salary__text}>
        Зарплата{' '}
        <span>
          <SortArrow />
        </span>
      </li>
      <li className={css.exp__text}>
        Опыт работы{' '}
        <span>
          <SortArrow />
        </span>
      </li>
      <li className={css.rask__text}>
        Расклад{' '}
        <span>
          <SortArrow />
        </span>
      </li>
      <li className={css.acc__text}>
        Отклик{' '}
        <span>
          <SortArrow />
        </span>
      </li>
      <li className={css.emp__text}>Занятость</li>
      <li className={css.contacts__text}>Контакты</li>
      <li>Действия</li>
    </ul>
  );
};
