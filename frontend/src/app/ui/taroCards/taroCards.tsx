import css from './taroCards.module.css';

type TaroCardsProps = {
  text: string;
  check: boolean;
};

export const TaroCards = ({ text, check }: TaroCardsProps) => {
  return (
    <div className={css.main__container}>
      <div className={check ? css.image : css.noactive} />
      <i className={css.main__content}>{text}</i>
    </div>
  );
};
