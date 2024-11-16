import css from './taroCards.module.css';

type TaroCardsProps = {
  text: string;
  image: string;
};

export const TaroCards = ({ text, image = '' }: TaroCardsProps) => {
  return (
    <div
      className={css.main__container}
      style={image.length !== 0 ? { '--image-url': `url(${image})` } : {}}
    >
      <span className={css.main__content}>{text}</span>
    </div>
  );
};
