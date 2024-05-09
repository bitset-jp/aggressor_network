# -*- coding: utf-8 -*-

class Setting:
  # デバイス名
  dev = None

  # キャパシティ
  limit = None
  limit_backup = 1000

  # 遅延: TIME [ JITTER [CORRELATION]]
  delay = None

  # ロス: PERCENT
  loss = None

  #重複: PERCENT
  duplicate = None

  #破壊(データ破壊): PERCENT
  corrupt = None

  #再送: PERCENT
  reorder = None

  # 帯域
  rate = None

  def __init__(self, dev):
    self.dev = dev


  def __str__(self):

    if self.is_changed():
      return "limit:{} delay:{} loss:{} duplicate:{} corrupt:{} reorder:{} rate:{}".format(
        ("-" if self.limit is None else self.limit),
        ("-" if self.delay is None else self.delay),
        ("-" if self.loss is None else self.loss),
        ("-" if self.duplicate is None else self.duplicate),
        ("-" if self.corrupt is None else self.corrupt),
        ("-" if self.reorder is None else self.reorder),
        ("-" if self.rate is None else self.rate)
      )
    else:
      return "-------"

  def clone(self):
    dst = Setting(self.dev)
    dst.limit = self.limit
    dst.limit_backup = self.limit_backup
    dst.delay = self.delay
    dst.loss = self.loss
    dst.duplicate = self.duplicate
    dst.corrupt = self.corrupt
    dst.reorder = self.reorder
    dst.rate = self.rate
    return dst

  def clear(self):
    if self.limit is not None:
      self.limit_backup = self.limit

    self.limit = None
    self.delay = None
    self.loss = None
    self.duplicate = None
    self.corrupt = None
    self.reorder = None
    self.rate = None


  def is_changed(self):
    return True if (self.limit is not None or
                    self.delay is not None or
                    self.loss is not None or
                    self.duplicate is not None or 
                    self.corrupt is not None or 
                    self.reorder is not None or
                    self.rate is not None ) else False


  def get_limit(self):
    #return 1000 if self.limit is None else self.limit
    if self.limit is not None:
      return self.limit
    elif self.limit_backup is not None:
      return self.limit_backup

    return 1000
      

  def set_limit(self, args):
    '''
    1. キャパシティ limit:
    '''
    self.limit = args[0] if args else None

  def set_delay(self, args):
    '''

    1. TIME:    遅延時間 (s/ms/us)   default:us
    2. JITTER:  ゆらぎ (s/ms/us)     default:us
    3. RANDOM:  発生率 (%)           default:%
    '''
    self.delay = args if args else None


  def set_loss(self, args):
    '''
    1. ロス率(%) default:%
    '''
    self.loss = args if args else None


  def set_duplicate(self, args):
    '''
    1. 重複率(%) default:%
    '''
    self.duplicate = args if args else None


  def set_corrupt(self, args):
    '''
    1. 破損率(%) default:%
    '''
    self.corrupt = args if args else None


  def set_reorder(self, args):
    '''
    1. 再送率(%) default:%

    delay が指定されていること
    '''
    self.reorder = args if args else None


  def set_rate(self, args):
    '''
    1. 帯域 (T/G/M/K/'' bit/bps) ... default: bit
    '''
    self.rate = args if args else None


  def validate(self):

    if self.delay is None and self.reorder is not None:
      return (False, "reordering not possible without specifying some delay")

    return (True, None)