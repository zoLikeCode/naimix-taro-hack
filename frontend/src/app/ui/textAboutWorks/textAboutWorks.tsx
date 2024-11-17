import css from './textAboutWorks.module.css';

export const TextAboutWorks = ({ text }: { text: string }) => {
  return (
    <div className={css.main__container}>
      {/* <p className={css.years__works}>2022 - 2023</p>
      <h3 className={css.name__company}>Компания “Astrology”</h3> */}
      <p className={css.desc__works}>{text}</p>
    </div>
  );
};
