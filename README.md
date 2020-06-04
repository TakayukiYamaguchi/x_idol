必要なライブラリ

pip install janome
 
pip install gensim

keras

engineのchatbot.pyを実行すると、botと会話できる。(マルコフ連鎖で文章を生成,終了する場合はquitで終了できる。)

bot_chat.pyではチャットボット同士の会話が見られる。（botは会話を3ラリーだけする。最初bot1に与えられるワードは"魔法"）

vector.pyでは、bot_chat.pyでのbot1の出力する文章を分かち書きにし、ベクトル化した値で会話を行っている。

vector.pyでは、bot1,bot2共に文章をベクトル化した値を出力し会話を行う。