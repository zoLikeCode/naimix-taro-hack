import { SortArrow } from '../../../../public/SortArrow';
import css from './attrRasklText.module.css';

export const AttrRasklText = () => {
  return (
    <ul className={css.main__container}>
      <li>
        Дата{' '}
        <span>
          <SortArrow />
        </span>
      </li>
      <li>
        ФИО{' '}
        <span>
          <SortArrow />
        </span>
      </li>
      <li>
        Профессия{' '}
        <span>
          <SortArrow />
        </span>
      </li>
      <li>
        Опыт{' '}
        <span>
          <SortArrow />
        </span>
      </li>
      <li>Место </li>
      <li>Действия</li>
    </ul>
  );
};
