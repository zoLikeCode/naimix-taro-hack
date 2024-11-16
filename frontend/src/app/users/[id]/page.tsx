'use client';

import { DescriptionText, StaffBlock, TaroCards, TextAboutWorks } from '@/app/ui';
import css from './page.module.css';
import { useState } from 'react';
import RadarCharts from '@/app/ui/radarCharts/radarCharts';

const TEMP_TEXT: string =
  'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.';

const Page = () => {
  const [fastTaro, setFastTaro] = useState<boolean>(false);

  const taroLists = [
    'https://psv4.userapi.com/s/v1/d/KBFnmf4hgYxkErvQx742ZNBWbBdNY_-FLmbC701ECmrZoI7w8FyZDarx_SJ7nZTNQNbWxDsTqR4m_SRjId_kKqevu7XJnFToaCT-zSM_NxnDYmPyYo3VRQ/TARO_RAJDERA-UAJTA_pdf-image-171.png',
    '',
    '',
  ];

  return (
    <div className={css.main__container}>
      <div className={css.info__container}>
        <div className={css.info__meta}>
          <div className={css.info__avatar} />
          <div className={css.info__buttons__list__container}>
            <button className={css.info__button__list}>Сделать расклад</button>
            <button className={css.info__button__list}>Проверить совместимость</button>
            <button className={css.info__button__list}>
              Характеристика о прошлых местах работы
            </button>
          </div>
        </div>
        <div className={css.info__contacts}>
          <h3>Александр Евстигнеев</h3>
          <h4>Продуктовый менеджер</h4>
          <div className={css.info__contacts__meta__block}>
            <div className={css.info__contacts__meta__phone}>
              <h5 className={css.h5__text}>Телефон</h5>
              <p>+7-926-234-56-78</p>
            </div>
            <div className={css.info__contacts__meta__email}>
              <h5 className={css.h5__text}>Почта</h5>
              <p>pochta@mail.ru</p>
            </div>
            <div className={css.info__contacts__meta__birthday}>
              <h5 className={css.h5__text}>Дата рождения</h5>
              <p>04.03.1986</p>
            </div>
            <div className={css.info__contacts__meta__city}>
              <h5 className={css.h5__text}>Город</h5>
              <p>Ростов-на-дону</p>
            </div>
            <div className={css.info__contacts__meta__levels}>
              <h5 className={css.h5__text}>Образование</h5>
              <p>МГУ им. Ломоносова, Эконом. ф.</p>
            </div>
          </div>
          <div className={css.info__contacts__sammary}>
            <h5 className={css.h5__text}>Краткое саммари резюме</h5>
            <p>
              Специалист в продуктовом менеджменте с общим стажем более 7 лет. Навыки работы в 1С,
              Excel, PowerPoint, Outlook. Ответственен, пунктуален. Повысил прибыль на 6% в компании
              “Astrology”. Автор менеджерских курсов.
            </p>
          </div>
          <span>
            <button type="button" className={css.more__info}>
              Подробнее
            </button>
          </span>
        </div>
        <div className={css.info__works}>
          <h5 className={css.h5__text}>Опыт работы</h5>
          <TextAboutWorks />
          <TextAboutWorks />
          <span>
            <button type="button" className={css.more__info}>
              Ещё
            </button>
          </span>
        </div>
      </div>
      <div className={css.taro__container}>
        <div className={css.taro__lists}>
          {taroLists.map((taro: string, index: number) => {
            return <TaroCards key={index} text={`${index + 1}`} image={taro} />;
          })}
        </div>
        <div className={css.taro__buttons__container}>
          <button
            className={fastTaro == false ? css.taro__button__active : css.taro__button}
            type="button"
            onClick={() => {
              setFastTaro(!fastTaro);
            }}
          >
            Быстрый расклад
          </button>
          <button
            className={fastTaro == true ? css.taro__button__active : css.taro__button}
            type="button"
            onClick={() => {
              setFastTaro(!fastTaro);
            }}
          >
            Полный расклад
          </button>
        </div>
        <div className={css.taro__chooses}>
          {Array.from({ length: 78 }, (_, index) => (
            <div
              onClick={() => {
                console.log(index);
              }}
              className={css.taro__choosesCards}
              key={index}
              style={{
                top: `${20 * (index % 20)}px`,
                left: `${Math.floor(index / 20) * 100}px`,
                zIndex: 20 + (index % 20),
              }}
            />
          ))}
        </div>
      </div>
      <div className={css.parcel__container}>
        <h5 className={css.h5__text}>Краткое толкование общего расклада</h5>
        <DescriptionText text={TEMP_TEXT} />
        <h5 className={css.h5__text}>Полное толкование расклада</h5>
        <div className={css.parcel__buttons__block}>
          <button className={css.parcel__button}>Общее</button>
          <button className={css.parcel__button}>Карта 1</button>
          <button className={css.parcel__button}>Карта 2</button>
          <button className={css.parcel__button}>Карта 3</button>
        </div>
      </div>
      <div className={css.recommendations__container}>
        <h5 className={css.h5__text}>Рекомендации по общению с кандидатом</h5>
        <DescriptionText text={TEMP_TEXT} />
        <h5 className={css.h5__text}>Прогноз проявления в коллективе</h5>
        <p className={css.recommendations__description}>{TEMP_TEXT}</p>
      </div>
      <div className={css.best__match__container}>
        <h5 className={css.h5__text}>Сотрудники, с которыми сработается лучше всего </h5>
        {Array.from({ length: 5 }, (_, index) => (
          <StaffBlock key={index} />
        ))}
      </div>
    </div>
  );
};

export default Page;
