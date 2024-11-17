import UpArrow from '../../../../public/UpArrow';
import css from './popupFilter.module.css';

type PopupFilterProps = {
  active: boolean;
  setActive: (value: boolean) => void;
  store: string | number;
  setStore: any;
  data: string[] | number[];
  type: string;
};

export const PopupFilter = ({
  active,
  setActive,
  data,
  store,
  setStore,
  type,
}: PopupFilterProps) => {
  return (
    <ul
      className={
        active ? (type === 'str' ? css.main__container : css.main__container__num) : css.noactive
      }
    >
      {data.map((elem, index: number) => (
        <li
          key={index}
          onClick={() => {
            setActive(false);
            setStore(elem);
          }}
        >
          {elem}
        </li>
      ))}
    </ul>
  );
};
