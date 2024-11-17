import Link from 'next/link';
import css from './page.module.css';
import { PopupMenuNav } from './ui';

export default function Home() {
  return (
    <div className={css.main__container}>
      <p>Добро пожаловать в сервис</p>
      <div className={css.buttons__container}>
        <Link href="/candidates">
          {' '}
          <button type="button">Перейти к кандидатам</button>
        </Link>
        <Link href="/history">
          {' '}
          <button type="button">Перейти к истории раскладов</button>
        </Link>
      </div>
    </div>
  );
}
