/******************************************
 ** CAREFUL WHEN CHANGING BELOW THIS LINE **
 ******************************************/
var restapi = "rest/";

function getConfigurations() {
  var confs = {
    global: {
      indexViewId: "yornShakeitView",
      maxShakes: 99,
      swipeThreshold: 5,
      swipeCardsThreshold: 15,
      totalCards: 60,
      totalAchievements: 9,
      imagesFolder: "app/assets/images",
      translateTextsFile: "app/assets/texts/pt.json",
      shakePageShakeBtTimeout: 7,
      mysteryBoxStatusTimeout: 60, // ttl for cached mysterybox status in seconds
      videoPlaybackCountdown: 5, // ttl to freeze the carousel and show the video playback. Value in seconds.
      version: "3.0.0",
      tutorialHasCloseButton: "true",
      isGuessCardNameActive: true // Flag to activate/de-activate globally the Guess name functionality
    },
    mainShake: {
      threshold: 10,
      validationTime: 1,
      minValidThresholds: 5
    },

    events: {
      closeTutorial: "event_closeTutorial",
      closeVideo: "event_closeVideo",
      closeTerms: "event_closeTerms",
      cardRedeemAction: "event_cardRedeemAction",
      cardClose: "event_cardClose",
      prizeAnswerWrong: "event_prizeAnswerWrong",
      swipeLeft: "event_swipeLeft",
      swipeRight: "event_swipeRight",
      swipeUp: "event_swipeUp",
      swipeDown: "event_swipeDown",
      update_userprize: "update.userprize",
      updateUserShakesStatus: "event_updateUserShakesStatus",
      submiteUpdateProfileUserPrizes: "event_submiteUpdateProfileUserPrizes",
      updateListOfDuplicatedCards: "event_updateListOfDuplicatedCards",
      updateLogin: "event_updateLogin",
      updateMysteryBox: "event_updateMysteryBox",
      openMysteryBox: "event_openMysteryBox",
      placeContainerShakePosition: "event_placeContainerShakePosition"
    },
    cardTypes: {
      joker: "JOKER",
      collection: "COLLECTION",
      gold: "GOLD"
    },
    routesParameters: {
      option: "option",
      shake: "shake",
      duplicatedgold: "duplicatedgold",
      middlePrizeNotShuffled: "middleprize",
      msisdn: "msisdn"
    },
    routes: {
      achievements: "achievements",
      landingPage: "main",
      booklet: "booklet",
      error: "error",
      exchangetype: "exchangetype",
      cardsexchange: "cardsexchange",
      exchangecardsforwildcard: "exchangecardsforwildcard",
      exchangefriends: "exchangefriends",
      exchangecardfriend: "exchangecardfriend",
      prizes: "prizes",
      winshakes: "referral",
      profile: "profile",
      history: "history",
      terms: "terms",
      mysterybox: "mysterybox",
      previousbooklet: "previousbooklet",
      qrcode: "qrcode",
      promocode: "promocode"
    },
    defaultError: {
      statusCode: 404,
      statusMessage: "page not found"
    },
    statusCode: {
      TIMEOUT: -1,
      SERVER_ERROR: 500,
      SUCCESS: 0,
      ERROR: 1,
      ERROR_AUTH_INVALID_PARAMETERS: 2,
      ERROR_AUTH_INVALID_TARIFF: 3,
      ERROR_USER_INACTIVE: 5,
      ERROR_COLLECTION_INACTIVE: 6,
      ERROR_NO_SHAKES_AVAILABLE: 7,
      ERROR_SESSION_EXPIRED: 9,
      ERROR_TERMS_NOT_ACCEPTED: 11,
      ERROR_USER_BLACKLISTED: 14,
      ERROR_AUTH_HOTLINE_PRE_PAID : 41,
      ERROR_AUTH_HOTLINE_POST_PAID: 42,
      ERROR_DUPLICATED_GOLD_CARDS: 101,
      ERROR_REDEEM_FORM: 102,
      SKIP_DUPLICATED_GOLD_CARDS: 103,
      INFO_NEW_ACHIEVEMENT: 201,
      WARNING_USER_MIDDLE_PRIZE_NOT_SHUFFLED_FOUND: 202,
      ERROR_QR_CODE_MESSAGE: 305,
      ERROR_PROMO_CODE_MESSAGE: 306,
      ERROR_EXCHANGE_CARDS_DISABLED: 307,
      ERROR_PRIZE_NOT_EXISTS: 308,
      ERROR_EXCHANGE_DUPLICATED_LIST_NUMBER: 309
    },
    criticalErrors: [],
    expiredSessionErrors: [],
    restapi: restapi,
    endpoint: {
      achievements: "achievements",
      booklet: "cards",
      checkachievements: "achievements/check",
      duplicatedGoldCard: "prizes/gold/duplicated",
      eligibleprizes: "user/eligibleprizes",
      exchangecardsshake: "cards/exchange/shake",
      exchangegoldcard: "prizes/gold/exchange?selectedUserPrizeId=:selectedUserPrizeId",
      history_prizes: "history/prizes",
      history_plays: "history/plays",
      keepAlive: "general/keepalive",
      prizelist: "general/prizelist",
      prizeRedeem: "prizes/redeem",
      shuffleMiddlePrizeCards: "prizes/shuffleMiddlePrizeCards",
      prizeTermsAcceptance: "prizes/acceptance",
      profileAchievements: "achievements/persist",
      profileShakes: "user/profile/shakes",
      question: "question",
      questionValidation: "question/validate",
      referral: "referral",
      remote_properties: "general/properties",
      shakes_available: "shakes/available",
      shakes_new: "shakes/new",
      shakes_shake: "shakes/shake",
      splashscreens: "general/splashscreens",
      termsAndConditions: "terms",
      termsAcceptance: "terms/acceptance",
      tutorials: "tutorials",
      tutorialsCompleted: "tutorials/completed",
      userFirstlogin: "user/firstlogin",
      userPrizes: "user/prizes",
      validateReferral: "referral/:code",
      validateRefferralCode: "referral/:code",
      texts: "general/texts",
      address: "general/address/:cp4/:cp3",
      listOfDuplicatedCards: "cards/listduplicated",
      exchangeCardsForPrize: "cards/exchange/prize",
      exchangeCardsInitialize: "cards/exchange/initialize",
      exchangeCardsFriendInfo: "cards/exchange/friend/info",
      connectToFriend: "cards/exchange/friend/start",
      checkStatusFriend: "cards/exchange/friend/status",
      abortExchangeCardFriend: "cards/exchange/friend/abort",
      selectCard: "cards/exchange/friend/selectcard",
      confirmTrade: "cards/exchange/friend/confirm",
      statusMysteryBox: "mbox/status",
      openMysteryBox: "mbox/open",
      userInfo: "user/cat/:msisdn",
      userStatus: "user/status",
      saveFacebookInfo: "user/facebooklogin",
      saveNickName: "user/nickname",
      previousbooklet: "cards/previouscollection",
      sendQrCodeCampaignCode: "campaigns/redeem",
      guessCardName: "cards/guessname",
      promotionsredeem: "promotions/redeem",
      userSettings: "user/settings"
    }
  };

  confs.expiredSessionErrors = [
    confs.statusCode.ERROR_AUTH_INVALID_PARAMETERS,
    confs.statusCode.ERROR_USER_INACTIVE,
    confs.statusCode.ERROR_SESSION_EXPIRED
  ];

  confs.criticalErrors = [
    confs.statusCode.ERROR_AUTH_INVALID_PARAMETERS,
    confs.statusCode.ERROR_AUTH_INVALID_TARIFF,
    confs.statusCode.ERROR_USER_INACTIVE,
    confs.statusCode.ERROR_SESSION_EXPIRED,
    confs.defaultError.statusCode
  ];

  return confs;
}

/********** Do not change below this point! **********/
angular.module("app.config", []).provider("appConfig", [AppConfigurations]);

function AppConfigurations() {
  this.$get = function() {
    return getConfigurations();
  };
}
