import { create } from 'zustand';

type useShowCountProps = {
  count: number;
  setCount: (value: number) => void;
};

export const useShowCount = create<useShowCountProps>((set) => ({
  count: 10,
  setCount: (newCount) => set(() => ({ count: newCount })),
}));

type useChooseExperienceProps = {
  experience: string;
  setExperience: (value: string) => void;
};

export const useChooseExperience = create<useChooseExperienceProps>((set) => ({
  experience: 'Опыт работы',
  setExperience: (exp) => set(() => ({ experience: exp })),
}));

type useChooseEmploymentProps = {
  employment: string;
  setEmployment: (value: string) => void;
};

export const useChooseEmployment = create<useChooseEmploymentProps>((set) => ({
  employment: 'Занятость',
  setEmployment: (emp) => set(() => ({ employment: emp })),
}));

type useChooseScheduleProps = {
  schedule: string;
  setSchedule: (value: string) => void;
};

export const useChooseSchedule = create<useChooseScheduleProps>((set) => ({
  schedule: 'График',
  setSchedule: (sch) => set(() => ({ schedule: sch })),
}));

type useChooseSortProps = {
  sort: string;
  setSort: (value: string) => void;
};

export const useChooseSort = create<useChooseSortProps>((set) => ({
  sort: 'Сначала новые',
  setSort: (srt) => set(() => ({ sort: srt })),
}));
