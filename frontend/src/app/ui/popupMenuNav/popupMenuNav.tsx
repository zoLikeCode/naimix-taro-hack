import Link from 'next/link';
import css from './popupMenuNav.module.css';

type PopupMenuNavProps = {
  active: boolean;
  setActive: (value: boolean) => void;
};

export const PopupMenuNav = ({ active, setActive }: PopupMenuNavProps) => {
  return (
    <div className={true ? css.main__container : css.noactive}>
      <h2>Меню:</h2>
      <li>
        <Link href="/candidates">Кандидаты</Link>
      </li>
      <li>
        <Link href="/history">История</Link>
      </li>
    </div>
  );
};
