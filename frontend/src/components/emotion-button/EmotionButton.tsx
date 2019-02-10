import * as React from 'react';
import cn from 'classnames';
import styles from './EmotionButton.module.css';

export interface EmotionButtonProps {
  icon?: React.ReactNode;
  caption: string;
  type?: string;
  highlight?: boolean;
  onClick?: () => any;
}

const EmotionButton: React.SFC<EmotionButtonProps> = ({
  icon,
  caption,
  highlight,
  ...rest
}) => {
  return (
    <button
      className={cn(styles.button, {[styles.buttonHighlight]: highlight})}
      {...rest}
    >
      <span className={styles.icon}>{icon}</span>
      <span className={styles.caption}>{caption}</span>
    </button>
  );
};

export default EmotionButton;
