'use client';

import { DescriptionText, StaffBlock, TaroCards, TextAboutWorks } from '@/app/ui';
import css from './page.module.css';
import { useEffect, useState } from 'react';
import RadarCharts from '@/app/ui/radarCharts/radarCharts';
import { GetProfile } from '@/app/lib/getProfile';
import { usePathname, useSearchParams } from 'next/navigation';
import Link from 'next/link';
import { postAnswer, postTaroSpread } from '@/app/lib/postTaroSpead';
import { GetTaroCards } from '@/app/lib/getTaroCards';
import { GetTaro } from '@/app/lib/getTaro';
import { postCompetency } from '@/app/lib/postCompetency';

const Page = () => {
  const [fastTaro, setFastTaro] = useState<boolean>(false);

  const [user, setUser] = useState();

  const [activeMoreInfo, setActiveMoreInfo] = useState<boolean>(false);
  const [activeMoreWorks, setActiveMoreWorks] = useState<boolean>(false);
  const [showHelper, setShowHelper] = useState<boolean>(true);
  const [showRadar, setShowRadar] = useState<boolean>(false);

  const [photo, setPhoto] = useState([]);

  const id: string = usePathname();

  const [taroLists, setTaroLists] = useState(0);
  const [value, setValue] = useState('');

  const [cardsInfo, setCardsInfo] = useState([]);

  const [nowButton, setNowButton] = useState(0);

  const [skills, setSkiils] = useState({});

  const taroInfoLines = cardsInfo?.taro_info?.split('\n') || [];

  // useEffect(() => {
  //   setTaroLists(3);
  // }, [photo]);

  useEffect(() => {
    if (fastTaro && taroLists == 1) {
      const PostTaro = async (id) => {
        const response = await postTaroSpread('compatibility', id.replace('/users/', ''));
        const response_two = await postAnswer({ question: value });
      };
      if (id) {
        PostTaro(id);
      }
    }
    if (taroLists == 3) {
      const PostTaro = async (id) => {
        const response = await postTaroSpread('three', id.replace('/users/', ''));
        const response_two = await postAnswer({ question: value });
        const arr = response.cards.split(',');
        setPhoto(arr);
      };
      if (id) {
        PostTaro(id);
      }
    }
  }, [taroLists]);
  useEffect(() => {
    const LoadProfiles = async (id) => {
      if (!id) return;
      const response = await GetTaro({ id: id.replace('/users/', '') });
      if (response.result == null) {
        const response_two = await GetProfile({ id: id.replace('/users/', '') });
        setUser(response_two);
      } else {
        const response_three = await postCompetency(id.replace('/users/', ''));
        setUser(response.result.user_profile);
        setCardsInfo(response.result);
        setSkiils(response_three);
      }
    };
    LoadProfiles(id);
  }, [id]);
  return (
    <div className={css.main__container}>
      <div className={css.info__container}>
        <div className={css.info__meta}>
          <div className={css.info__avatar} />
          <div className={css.info__buttons__list__container}>
            <button
              className={css.info__button__list}
              type="button"
              onClick={() => {
                window.scrollBy({ top: 600, behavior: 'smooth' });
              }}
            >
              Сделать расклад
            </button>
            <Link href="/candidates">
              <button className={css.info__button__list}>Проверить совместимость</button>
            </Link>
            <button className={css.info__button__list}>
              Характеристика о прошлых местах работы
            </button>
          </div>
        </div>
        <div className={css.info__contacts}>
          <h3>{user?.full_name}</h3>
          <h4>{user?.prof}</h4>
          <div className={css.info__contacts__meta__block}>
            <div className={css.info__contacts__meta__phone}>
              <h5 className={css.h5__text}>Телефон</h5>
              <p>{user?.phone_number}</p>
            </div>
            <div className={css.info__contacts__meta__email}>
              <h5 className={css.h5__text}>Почта</h5>
              <p title={user?.email}>{user?.email}</p>
            </div>
            <div className={css.info__contacts__meta__birthday}>
              <h5 className={css.h5__text}>Дата рождения</h5>
              <p>{user?.birthday}</p>
            </div>
            <div className={css.info__contacts__meta__city}>
              <h5 className={css.h5__text}>Город</h5>
              <p title={user?.city}>{user?.city}</p>
            </div>
            <div className={css.info__contacts__meta__levels}>
              <h5 className={css.h5__text}>Образование</h5>
              <p title={user?.education}>{user?.education}</p>
            </div>
          </div>
          <div className={css.info__contacts__sammary}>
            <h5 className={css.h5__text}>Краткое саммари резюме</h5>
            <p>{user?.summary_by_resume}</p>
          </div>
          <span>
            <button
              type="button"
              className={activeMoreInfo ? css.noactive : css.more__info}
              onClick={() => {
                setActiveMoreInfo(true);
              }}
            >
              Подробнее
            </button>
          </span>
          <div className={activeMoreInfo ? css.more__info__container : css.noactive}>
            <div
              className={
                JSON.stringify(skills) === '{}' ? css.more__info__container__helper : css.noactive
              }
            >
              <div className={css.more__info__container__helper__image} />
              <p>Здесь появится саммари расклада и карта компетенций после расклада таро</p>
            </div>
            <div className={JSON.stringify(skills) !== '{}' ? css.more__info__radar : css.noactive}>
              <RadarCharts
                points={[
                  skills?.flexibility,
                  skills?.stress_resistance,
                  skills?.creativity,
                  skills?.leadership_qualities,
                  skills?.ability_decisions,
                  skills?.organizational_skills,
                  skills?.teamwork,
                  skills?.communication_skills,
                  skills?.initiative,
                  skills?.professional_competence,
                  skills?.hard_work,
                  skills?.productivity,
                ]}
              />
            </div>
            <span>
              <button
                type="button"
                className={activeMoreInfo ? css.more__info__up : css.noactive}
                onClick={() => {
                  setActiveMoreInfo(false);
                }}
              >
                Свернуть
              </button>
            </span>
          </div>
        </div>
        <div className={css.info__works}>
          <h5 className={css.h5__text}>Опыт работы</h5>
          <TextAboutWorks text={user?.job_experience} />
          <span>
            {/* <button
              type="button"
              className={activeMoreWorks ? css.noactive : css.more__info}
              onClick={() => {
                setActiveMoreWorks(true);
                setActiveMoreInfo(true);
              }}
            >
              Ещё
            </button> */}
          </span>
          {/* <span>
            <button
              type="button"
              className={activeMoreWorks ? css.more__info__works : css.noactive}
              onClick={() => {
                setActiveMoreWorks(false);
              }}
            >
              Свернуть
            </button>
          </span> */}
        </div>
      </div>
      <div className={css.taro__container}>
        {fastTaro ? (
          <div className={css.taro__lists_fast}>
            {taroLists >= 1 ? <TaroCards check={true} /> : <TaroCards text={`1`} />}
          </div>
        ) : (
          <div className={css.taro__lists}>
            {taroLists >= 1 ? <TaroCards check={true} /> : <TaroCards text={`1`} />}
            {taroLists >= 2 ? <TaroCards check={true} /> : <TaroCards text={`2`} />}
            {taroLists == 3 ? <TaroCards check={true} /> : <TaroCards text={`3`} />}
          </div>
        )}
        <div className={css.taro__buttons__container}>
          <button
            className={css.taro__button}
            type="button"
            onClick={() => {
              setFastTaro(true);
              setTaroLists(0);
            }}
          >
            Быстрый расклад на кандидата
          </button>
          <button
            className={css.taro__button}
            type="button"
            onClick={() => {
              setFastTaro(false);
              setTaroLists(0);
            }}
          >
            Полный расклад на кандидата
          </button>
        </div>
        <form className={css.taro__forms}>
          <input
            placeholder="Задать свой вопрос"
            className={css.taro__inputs}
            onChange={(e) => {
              setValue(e.target.value);
            }}
          />
        </form>
        <div className={css.taro__chooses}>
          {Array.from({ length: 78 }, (_, index) => (
            <div
              onClick={() => {
                if (fastTaro ? taroLists < 1 : taroLists < 3) {
                  setTaroLists(taroLists + 1);
                }
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
        {/* <h5 className={css.h5__text}>Краткое толкование общего расклада</h5>
        <DescriptionText text={TEMP_TEXT} /> */}
        <h5 className={css.h5__text}>Полное толкование расклада</h5>
        <div className={css.parcel__buttons__block}>
          <button className={css.parcel__button}>Общее</button>
          <button className={css.parcel__button}>Карта 1</button>
          <button className={css.parcel__button}>Карта 2</button>
          <button className={css.parcel__button}>Карта 3</button>
        </div>
        {taroInfoLines.length === 0 ? (
          <p>Нет информации</p>
        ) : (
          <>
            <p>{taroInfoLines[0] || ''}</p>
            <p>{taroInfoLines[2] || ''}</p>
            <p>{taroInfoLines[4] || ''}</p>
            <p>{taroInfoLines[6] || ''}</p>
            <p>{taroInfoLines[8] || ''}</p>
          </>
        )}
      </div>
      <div className={css.recommendations__container}>
        <h5 className={css.h5__text}>Рекомендации по общению с кандидатом</h5>
        <DescriptionText text={user?.recomendation} />
        <h5 className={css.h5__text}>Прогноз проявления в коллективе</h5>
        <p className={css.recommendations__description}>{}</p>
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
