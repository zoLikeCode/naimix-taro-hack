import css from './descriptionText.module.css';

export const DescriptionText = ({ text }: { text: string }) => {
  return <p className={css.main__container}>{text}</p>;
};
