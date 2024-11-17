import Link from 'next/link';
import { AcceptIcon } from '../../../../public/acceptIcon';
import css from './employeeInfo.module.css';

type EmployeeInfoProps = {
  name: string;
  salary: string;
  experience: string;
  contacts: string;
  id: string;
};

export const EmployeeInfo = ({ name, salary, experience, contacts, id }) => {
  return (
    <div className={css.main__container}>
      <div className={css.names__container}>
        <p className={css.name}>{name}</p>
        <p className={css.salary}>{salary}</p>
      </div>
      <p className={css.experience}>{experience}</p>
      <p className={css.rask}>
        <AcceptIcon />
      </p>
      <p className={css.acc}>
        <AcceptIcon />
      </p>
      <div className={css.worktime}>
        <p>Полный день, Неполный день, Гибкий график</p>
      </div>
      <div className={css.contacts}>
        <p>{contacts}</p>
      </div>
      <Link href={`/users/${id}`}>
        <button className={css.button} type="button">
          Подробнее
        </button>
      </Link>
    </div>
  );
};
