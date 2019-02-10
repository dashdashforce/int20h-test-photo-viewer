import * as React from 'react';
import styles from './EmotionFilter.module.css';
import EmotionButton from '../emotion-button/EmotionButton';
import FearIcon from '../emotion-button/FearIcon';
import HapinessIcon from '../emotion-button/HapinessIcon';
import NeutralIcon from '../emotion-button/NeutralIcon';
import SadIcon from '../emotion-button/SadIcon';
import SurpriseIcon from '../emotion-button/SurpriseIcon';
import DisgustIcon from '../emotion-button/DisgustIcon';
import AngryIcon from '../emotion-button/AngryIcon';
import CrossIcon from '../emotion-button/CrossIcon';

export interface EmotionFilterProps {
  current: string | null;
  onChange: (emotion: string | null) => any;
}

const EmotionFilter: React.SFC<EmotionFilterProps> = ({current, onChange}) => {
  return (
    <div className={styles.grid}>
      <div className={styles.item}>
        <EmotionButton
          type="button"
          icon={<FearIcon />}
          caption="Fear"
          highlight={current === 'fear'}
          onClick={() => onChange('fear')}
        />
      </div>
      <div className={styles.item}>
        <EmotionButton
          type="button"
          icon={<HapinessIcon />}
          caption="Hapiness"
          highlight={current === 'hapiness'}
          onClick={() => onChange('hapiness')}
        />
      </div>
      <div className={styles.item}>
        <EmotionButton
          type="button"
          icon={<NeutralIcon />}
          caption="Neutral"
          highlight={current === 'neutral'}
          onClick={() => onChange('neutral')}
        />
      </div>
      <div className={styles.item}>
        <EmotionButton
          type="button"
          icon={<SadIcon />}
          caption="Sadness"
          highlight={current === 'sadness'}
          onClick={() => onChange('sadness')}
        />
      </div>
      <div className={styles.item}>
        <EmotionButton
          type="button"
          icon={<SurpriseIcon />}
          caption="Surprise"
          highlight={current === 'surprise'}
          onClick={() => onChange('surprise')}
        />
      </div>
      <div className={styles.item}>
        <EmotionButton
          type="button"
          icon={<DisgustIcon />}
          caption="Disgust"
          highlight={current === 'disgust'}
          onClick={() => onChange('disgust')}
        />
      </div>
      <div className={styles.item}>
        <EmotionButton
          type="button"
          icon={<AngryIcon />}
          caption="Anger"
          highlight={current === 'anger'}
          onClick={() => onChange('anger')}
        />
      </div>
      {current && (
        <div className={styles.item}>
          <EmotionButton
            type="button"
            icon={<CrossIcon />}
            caption="Clear Filter"
            onClick={() => onChange(null)}
          />
        </div>
      )}
    </div>
  );
};

export default EmotionFilter;
