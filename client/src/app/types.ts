import { WordClass } from "./enums";

export type Translation = {
  name: string;
};

export type Word = {
  id: number;
  name: string;
  word_class: WordClass;
  name_accent: string;
  comment: string;
  usage: string;
  origin: string;
  translations: [Translation];
};

export type FormData = {
  name: { value: string };
  name_accent: { value: string };
  comment: { value: string };
  usage: { value: string };
  origin: { value: string };
};
